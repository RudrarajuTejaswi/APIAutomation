import requests
from utilities.configurations import getConfig
from utilities.endpoints import ApiResources

#this executes after each scenario defined in feature file
def after_scenario(context, scenario):
    #using tags to execute after_scenario to only few particular scenarios
    if 'libraryAPI' in scenario.tags:
        # deleting the book added above
        url_deleteBook = getConfig()['API']['base_url'] + ApiResources.deleteBook

        del_book_res = requests.post(url_deleteBook, json={"ID": context.book_id}, )  # headers are optional

        del_book_res_data = del_book_res.json()
        print(del_book_res_data)
        assert del_book_res_data.get('msg') == 'book is successfully deleted'
