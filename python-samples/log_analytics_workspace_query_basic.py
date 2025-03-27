from datetime import timedelta
import os
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
import pandas as pd
import json

#Set up the client
credential = DefaultAzureCredential()
client = LogsQueryClient(credential,connection_verify=False)

# Define the query
query = "AzureActivity | where Category == 'Administrative' | take 10"

# Execute the query
# Define the timespan (e.g., last 1 day)
timespan = timedelta(days=1)

# Execute the query
response = client.query_workspace(
    workspace_id="<REPLACE-WORKSPACE-ID>",
    query=query,
    timespan=timespan,

)

# Save the response to CSV files
for i, table in enumerate(response.tables):
    df = pd.DataFrame(table.rows, columns=table.columns)
    df.to_csv(f"output_{i}.csv", index=False)
    print(f"Results saved to output_{i}.csv")
