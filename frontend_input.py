import json
import ui
import backend
        
             
class QueryViewController(object):
    def __init__(self, qfdatasource, codatasource):
        self.v = ui.load_view('frontend_input')
        self.v.name = 'USPTO API Input'
        qf = self.v['queryfields']
        co = self.v['comparisons']
        of = self.v['outfields']
        
        qfds = ui.ListDataSource(items=qfdatasource)        
        cods = ui.ListDataSource(items=codatasource)
        self.ofds = ui.ListDataSource(items=qfdatasource)
        qf.data_source = qf.delegate = qfds
        co.data_source = co.delegate = cods
        of.data_source = of.delegate = self.ofds
        of.allows_multiple_selection = True
        
        qfds.action = self.qfds_action
        cods.action = self.cods_action
        self.v['btnadd2qry'].action = self.btnadd2qry_action
        self.v['btnsendquery'].action = self.btnsend2qry_action
        
        self.v.present('panel')
        
    def qfds_action(self, sender):
        self.v['lblquery'].text = sender.items[sender.selected_row]
    
    def cods_action(self, sender):
        self.v['lblcomparison'].text = sender.items[sender.selected_row]
        
    def btnadd2qry_action(self, sender):
        queryd = {self.v['lblcomparison'].text: {self.v['lblquery'].text: self.v['txtvalue'].text}}
        self.v['txtvquery'].text = ''.join([self.v['txtvquery'].text,
                                            json.dumps(queryd),
                                            '\n'])
                                            
    def btnsend2qry_action(self, sender):
        n = self.v['txtvquery'].text.count('\n')
        subquery0 = self.v['txtvquery'].text.replace('\n', ', ', n-1)
        subquery = subquery0.replace('\n', '')
        query = ''.join(['{"_and":[', 
                         subquery,
                         ']}'])
        fields = [self.ofds.items[rowtuple[1]] for rowtuple in
                  self.v['outfields'].selected_rows]
        print(fields)
        backend.input2output(query, fields) 
                                            

if __name__ == '__main__':
    qfds =[
           'appcit_app_number',
           'appcit_category',
           'appcit_date',
           'appcit_kind',
           'appcit_sequence',
           'app_country',
           'app_date',
           'app_number',
           'app_type',
           'assignee_city',
           'assignee_country',
           'assignee_first_name',
           'assignee_first_seen_date',
           'assignee_id',
           'assignee_last_name',
           'assignee_last_seen_date',
           'assignee_lastknown_city',
           'assignee_lastknown_country',
           'assignee_lastknown_latitude',
           'assignee_lastknown_location_id',
           'assignee_lastknown_longitude',
           'assignee_lastknown_state',
           'assignee_latitude',
           'assignee_location_id',
           'assignee_longitude',
           'assignee_organization',
           'assignee_sequence',
           'assignee_state',
           'assignee_total_num_patents',
           'assignee_type',
           'cited_patent_category',
           'cited_patent_date',
           'cited_patent_kind',
           'cited_patent_number',
           'cited_patent_sequence',
           'cited_patent_title',
           'citedby_patent_category',
           'citedby_patent_date',
           'citedby_patent_kind',
           'citedby_patent_number',
           'citedby_patent_title',
           'cpc_category',
           'cpc_first_seen_date',
           'cpc_group_id',
           'cpc_group_title',
           'cpc_last_seen_date',
           'cpc_section_id',
           'cpc_sequence',
           'cpc_subgroup_id',
           'cpc_subgroup_title',
           'cpc_subsection_id',
           'cpc_subsection_title',
           'cpc_total_num_assignees',
           'cpc_total_num_inventors',
           'cpc_total_num_patents',
           'inventor_city',
           'inventor_country',
           'inventor_first_name',
           'inventor_first_seen_date',
           'inventor_id',
           'inventor_last_name',
           'inventor_last_seen_date',
           'inventor_lastknown_city',
           'inventor_lastknown_country',
           'inventor_lastknown_latitude',
           'inventor_lastknown_location_id',
           'inventor_lastknown_longitude',
           'inventor_lastknown_state',
           'inventor_latitude',
           'inventor_location_id',
           'inventor_longitude',
           'inventor_sequence',
           'inventor_state',
           'inventor_total_num_patents',
           'ipc_action_date',
           'ipc_class',
           'ipc_classification_data_source',
           'ipc_classification_value',
           'ipc_first_seen_date',
           'ipc_last_seen_date',
           'ipc_main_group',
           'ipc_section',
           'ipc_sequence',
           'ipc_subclass',
           'ipc_subgroup',
           'ipc_symbol_position',
           'ipc_total_num_assignees',
           'ipc_total_num_inventors',
           'ipc_version_indicator',
           'nber_category_id',
           'nber_category_title',
           'nber_first_seen_date',
           'nber_last_seen_date',
           'nber_subcategory_id',
           'nber_subcategory_title',
           'nber_total_num_assignees',
           'nber_total_num_inventors',
           'nber_total_num_patents',
           'patent_abstract',
           'patent_average_processing_time',
           'patent_date',
           'patent_firstnamed_assignee_city',
           'patent_firstnamed_assignee_country',
           'patent_firstnamed_assignee_id',
           'patent_firstnamed_assignee_latitude',
           'patent_firstnamed_assignee_location_id',
           'patent_firstnamed_assignee_longitude',
           'patent_firstnamed_assignee_state',
           'patent_firstnamed_inventor_city',
           'patent_firstnamed_inventor_country',
           'patent_firstnamed_inventor_id',
           'patent_firstnamed_inventor_latitude',
           'patent_firstnamed_inventor_location_id',
           'patent_firstnamed_inventor_longitude',
           'patent_firstnamed_inventor_state',
           'patent_kind',
           'patent_num_cited_by_us_patents',
           'patent_num_claims',
           'patent_num_combined_citations',
           'patent_num_foreign_citations',
           'patent_num_us_application_citations',
           'patent_num_us_patent_citations',
           'patent_number',
           'patent_processing_time',
           'patent_title',
           'patent_type',
           'patent_year',
           'rawinventor_first_name',
           'rawinventor_last_name',
           'uspc_first_seen_date',
           'uspc_last_seen_date',
           'uspc_mainclass_id',
           'uspc_mainclass_title',
           'uspc_sequence',
           'uspc_subclass_id',
           'uspc_subclass_title',
           'uspc_total_num_assignees',
           'uspc_total_num_inventors',
           'uspc_total_num_patents'
                                       ]
    cods =[
           '_eq',
           '_neq',
           '_gt',
           '_gte',
           '_lt',
           '_lte',
           '_begins',
           '_contains',
           '_text_all',
           '_text_any',
           '_text_phrase'
           '_not',
           '_and',
           '_or'
               ]                                       
    QueryViewController(qfds, cods)

