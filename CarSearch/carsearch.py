import webbrowser

# List of URLs with filters applied
car_search_urls = [
    #cargurus keeps filters intact
    "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=m37&zip=60618",
    "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=m7&zip=60618#resultsPage=1",
    "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=m42&zip=60618#resultsPage=2",


    #carfax websites--- Add the fillers so it inputs your zip, milage, year, etc
    "https://www.carfax.com/Used-Toyota-SUVs_m33_bt8" #toyota carfax

]

def open_car_search_sites():
    """
    Opens all car search websites in the default web browser.
    """
    for url in car_search_urls:
        webbrowser.open(url)
        print(f"Opening: {url}")

if __name__ == "__main__":
    open_car_search_sites()
