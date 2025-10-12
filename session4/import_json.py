    # Task 5.4.1.2
    with open(r'..\helper\robot_data.json','r') as json_file:
        data=json.load(json_file)

    colors=data["colors"]
    robot_configurations = data["robot_configurations"]
