# BlogAPI


### python3 -m pip install -r requirements.txt


## Route Main  /api

## # /api/user/
    GET /api/user  
      -- show all Posts 
      ++ json(data[{'post':'','title':'','keys':'','date':''},...])
    GET /api/user/<ID>
      -- show post with Comment by id 
      ++ json({'post':'','title':'','keys':'','date':''})
    POST /api/user/<ID>
      -- add Comment To post 
      -- Data :
                + email 
                + comment < text >
      
## # /api/admin /
    ** headers {'username','password'}
    GET /api/admin/  
      -- show all Posts 
    GET /api/admin/<ID>
      -- show post with Comment by id 
    POST /api/admin/
        -- add new Post 
        -- Data :
                 + title
                 + post < text >
                 + keys 
    put /api/admin/<id> 
         -- edit post by id 
         -- data : 
                   + title | post | keys
               
  
      
     
