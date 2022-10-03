from atlassian import Confluence

confluence = Confluence(
    url='https://confluence.<your domain>.com', # Add your company domain
    token='CyperPunk EdgeRunners') # Token can be obtained from Profile > Settings

status = confluence.get_page_by_title(space='', title='') # Space and Title can be obtained from url of page
print(status)

status = confluence.update_page(
    parent_id= 69,
    page_id= 420,
    title='testpage',
    body='<p id="WindowsSignatureSet2.4.131.3-2-HandoffinstructionstoOperations">Test Text</p>'
) 
print(status)