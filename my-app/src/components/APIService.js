


export default class APIService {

    static UpdateArticle(article_id, body) {

        return fetch(`http://127.0.0.1:8000/api/articles/${article_id}/`, {
            'method':'PUT',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Token e35b33aa46701ebcc7db3882e1bee1ce62f9a31a'
              },
              body:JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static InsertArticle(body){

        return fetch('http://127.0.0.1:8000/api/articles/',{
            'method':'POST',
            headers: {
                'Content-Type':'application/json',
                'Authorization':'Token e35b33aa46701ebcc7db3882e1bee1ce62f9a31a'
              },
              body:JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static DeleteArticle(article_id) {
        return fetch(`http://127.0.0.1:8000/api/articles/${article_id}/`, {
            'method':'DELETE',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Token e35b33aa46701ebcc7db3882e1bee1ce62f9a31a'
              }
        })
    }

    static LoginUser(body){

        return fetch('http://127.0.0.1:8000/auth/ ',{
            'method':'POST',
            headers: {
                'Content-Type':'application/json',
              },
              body:JSON.stringify(body)
        }).then(resp => resp.json())
    }
}