import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    with open('./data/ipl_match.yaml','r') as my_file:
        data = yaml.load(my_file)
    # return data variable
    return data
