'''
This file contains the main logic of the Asset Manager web application.
'''
from tkinter import messagebox
from asset import Asset
# Create a list to store assets
assets = ['BajajAliiance Stock', 'Aditya Birla']
def add_asset(name):
    '''
    Add a new asset to the list.
    '''
    asset = Asset(name)
    assets.append(asset)
    messagebox.showinfo("Success", "Asset added successfully!")
def view_assets():
    '''
    View all the assets in the list.
    '''
    if len(assets) == 0:
        messagebox.showinfo("No Assets", "No assets found.")
    else:
        asset_names = [str(asset) for asset in assets]
        messagebox.showinfo("Assets", "\n".join(asset_names))
# Add your code here
add_asset("Google")
view_assets()