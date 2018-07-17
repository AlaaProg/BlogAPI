# BlogAPI


### python3 -m pip install -r requirements.txt




## Route /api/user/
    GET /api/user  
      -- show all Posts 
      ++ json(data[{'post':'','title':'','keys':'','date':''},...])
    GET /api/user/<ID>
      -- show post with Comment by id 
      ++ json('post':{'post':'','title':'','keys':'','date':''},'command':{'email':'','commadn':''})
    POST /api/user/<ID>
      -- add Comment To post 
      -- Data :
                + email 
                + comment < text >
      
## Route /api/admin /
    ** headers {'username','password'}
    GET /api/admin/  
      -- show all Posts 
      ++ json(data[{'post':'','title':'','keys':'','date':''},...])
    GET /api/admin/<ID>
      -- show post with Comment by id 
      ++ json('post':{'post':'','title':'','keys':'','date':''},'command':{'email':'','commadn':''})
    POST /api/admin/
        -- add new Post 
        -- Data :
                 + title
                 + post < text >
                 + keys 
    put /api/admin/<id> 
         -- edit post by id 
         -- data : 
                   + title OR post OR keys
    delete /api/admin/<id>
        -- delete post by id 
        
               
  
      
     
