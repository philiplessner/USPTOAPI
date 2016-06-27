import json
from io import StringIO
from typing import List, Dict, Any
import ui
import requests
from toolz import pluck
import pytablewriter


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
    
    
def input2query(queryfield: str, condition: str, value: str) -> Dict[str, Dict[str, str]]:
    return {condition:{queryfield:value}}


def join_queries(queries, join_condition='_and'):
    return {join_condition:queries}


if __name__ == '__main__':
#    query = {'_and': [{'_gte':{'patent_date':'2014-04-01'}}, {'_contains':{'assignee_organization':'KEMET'}}]}
    query1 = input2query('assignee_organization', '_contains', 'KEMET')
    query2 = input2query('patent_date', '_gte', '2014-04-01')
    query = join_queries([query1, query2], join_condition='_and')
    print(query)
    fields = ['patent_number', 'patent_title', 'patent_date']
    options = {'per_page':50}
    payload = make_query(query, fields, options)
    print('Query String\n', payload, '\n')
    r = get_info(payload)
    print('Encoded URL\n', r.url, '\n')
    print('Status Code\n', r.status_code, '\n')
    print('****Response****', '\n', r.json(), '\n\n')
    raw_output = get_output(fields, r.json())
    html_text = formated_output(fields, raw_output)
    v = ui.View()
    v.name = 'Test Web'
    web = ui.WebView()
    v.add_subview(web)
    web.height = 1024
    web.width = 720
    web.load_html(html_text)
    v.present('fullscreen')
