import pymongo

# Replace with your actual MongoDB connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Expense_Tracker"]  # Replace with your actual database name
collection = db["monthly_reports"]  # Replace with your actual collection name

def fetch_all_periods():
    """
    Fetches all unique periods stored in MongoDB.
    Ensures that there are no duplicates and returns a sorted list of periods.
    """
    # Fetch documents containing the 'period' field
    periods = collection.find({}, {"period": 1, "_id": 0})  # Only fetch the 'period' field
    periods_list = [item["period"] for item in periods if "period" in item]
    
    # Remove duplicates by converting the list to a set, then back to a list
    unique_periods = sorted(list(set(periods_list)))  
    
    return unique_periods

def insert_period(period, incomes, expenses, comment):
    """
    Insert a new document with the provided period, incomes, expenses, and comment into MongoDB.
    """
    document = {
        "period": period,
        "incomes": incomes,
        "expenses": expenses,
        "comment": comment
    }
    collection.insert_one(document)

def get_period(period):
    """
    Fetch a specific period's data from MongoDB.
    """
    return collection.find_one({"period": period}, {"_id": 0})
