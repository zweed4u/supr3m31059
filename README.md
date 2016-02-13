UPDATE  
New COMMIT  
-Py file now displays cw,size,& id in a formatted manner  

-Need a try catch for a redirect/No JSON object decoded for prior to release  

-Page visit for auth_token still needed  


=======================================================================

COMMIT 3: Added python alt  
-Allow for more user input  

-Grab product id as well as size ids in parse  

-Implement way to check for redirect before json parsing (step/loop to command redirect check)  

-parse cw info for name and ids (pretty print)  

-visit product page to scrape for auth_token  

-Prep url for POST  



=======================================================================


COMMIT 1:  
-Allow user to input size/url  

-Loop/step to line/if statement command again if redirect  

-Dummy id (parse json for ~productid and store for use in prefill)  

-Need to scrap auth_token for prefill (preliminary product page visit)  

-Proper prefill url POST request required:
http://www.supremenewyork.com/shop/16XXXX/add?utf8=%E2%9C%93&authenticity_token=N%2B7%2FbnfgYqZNVJRUsbJ%2BnOtb5%2FxsfOJ92bXli72bZzA%3D&size=25XXX&commit=add+to+cart  



