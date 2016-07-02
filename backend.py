import json
from io import StringIO
from typing import List, Dict, Any
import ui
import requests
from toolz import pluck
import pytablewriter
from outputviewcontroller import viewoutput


BASE_PATENT ='http://www.patentsview.org/api/patents/query'
BASE_ASSIGNEE = 'http://www.patentsview.org/api/assignees/query'


def make_query(query: str, fields: List[str], options: Dict[str, Any]) -> str:
    payload = ''.join(['q=', query,
                       '&f=', json.dumps(fields),
                       '&o=', json.dumps(options)])
    return payload
     

def get_info(payload: str, base=BASE_PATENT) -> Any:
    r = requests.get(BASE_PATENT, params=payload)
    if r.status_code == requests.codes.ok:
        return r
    else:
        r.raise_for_status()
    

def get_output(fields: List[str], response: Any) -> List[str]:
    patents = response['patents']
    return list(pluck(fields, patents))
    

def formated_output(fields: List[str], raw_output: List[str]) -> str:
    writer = pytablewriter.HtmlTableWriter()
    html_begin = '<!DOCTYPE HTML>\n<html>\n<body>\n'
    html_end = '\n</body>\n</html>'
    writer.table_name = 'Query Output\n'
    writer.header_list = fields
    writer.value_matrix = raw_output
    with StringIO() as f:
        f.write(html_begin)
        writer.stream = f
        writer.write_table()
        f.write(html_end)
        html_text = f.getvalue()
    return html_text

def input2output(query: str, fields: List[str]) -> None:
    options = {'per_page':50}
    payload = make_query(query, fields, options)
    print('Query String\n', payload, '\n')
    r = get_info(payload)
    print('Encoded URL\n', r.url, '\n')
    print('Status Code\n', r.status_code, '\n')
    print('****Response****', '\n', r.json(), '\n\n')
    raw_output = get_output(fields, r.json())
    html_text = formated_output(fields, raw_output)
    viewoutput(html_text)
