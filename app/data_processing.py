import pandas as pd

def process_costing_data(costing_df):
    grouped_costing = costing_df.groupby(['charge_code', 'account']).agg(
        friendly_name=('friendly_name', 'first'),
        ttl_costs_list=('ttl_costs', list),
        cost=('ttl_costs', 'sum')
    ).reset_index()

    nested_data = []
    for charge_code, group in grouped_costing.groupby('charge_code'):
        accounts = []
        total_cost = 0
        for _, row in group.iterrows():
            account_data = {
                'account': row['account'],
                'friendly_name': row['friendly_name'],
                'ttl_costs': row['ttl_costs_list'],
                'ac_total': row['cost']
            }
            accounts.append(account_data)
            total_cost += row['cost']

        nested_data.append({
            'charge_code': charge_code,
            'cc_total': total_cost,
            'accounts': accounts,
        })
    return nested_data

def process_master_data(master_df):
    grouped_master = master_df.groupby(['service', 'friendly_name']).agg(
        countOfServices=('service', 'size'),
        accountCost=('cost_for_service', 'sum')
    ).reset_index()

    nested_data = []
    for service, group in grouped_master.groupby('service'):
        accounts = []
        total_count = 0
        total_cost = 0
        for _, row in group.iterrows():
            account_data = {
                'friendly_name': row['friendly_name'],
                'countOfServices': row['countOfServices'],
                'accountCost': row['accountCost']
            }
            accounts.append(account_data)
            total_count += row['countOfServices']
            total_cost += row['accountCost']

        nested_data.append({
            'instanceName': service,
            'instanceCount': total_count,
            'service_cost': total_cost,
            'account': accounts
        })
    return nested_data
