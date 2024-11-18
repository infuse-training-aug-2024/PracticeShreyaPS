from azure.servicebus.management import ServiceBusAdministrationClient, SqlRuleFilter, SqlRuleAction
from dotenv import load_dotenv
import os

# Connection string to your Service Bus namespace
load_dotenv()
connection_string = os.getenv("NAMESPACE_CONNECTION_STR")
topic_name = os.getenv("TOPIC_NAME")

# Create a ServiceBusAdministrationClient instance
admin_client = ServiceBusAdministrationClient.from_connection_string(connection_string)

# Create a subscription with a SQL filter (color='blue' AND quantity=10)
subscription_name1 = "ColorBlueSize10Orders"
sql_filter1 = SqlRuleFilter("color = 'blue' AND quantity = 10")
admin_client.create_subscription(topic_name, subscription_name1)
admin_client.create_rule(
    topic_name=topic_name,
    subscription_name=subscription_name1,
    rule_name="BlueSize10Orders",
    filter=sql_filter1
)

# Create a rule with a SQL filter (color='red') and an action to modify quantity
subscription_name2 = "ColorRedOrders"
sql_filter2 = SqlRuleFilter("user.color = 'red'")
sql_action2 = SqlRuleAction("SET quantity = quantity / 2;")
admin_client.create_subscription(topic_name, subscription_name2)
admin_client.create_rule(
    topic_name=topic_name,
    subscription_name=subscription_name2,
    rule_name="RedOrdersWithAction",
    filter=sql_filter2,
    action=sql_action2
)

print("Subscriptions and rules created successfully.")
