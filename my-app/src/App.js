import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react'
import ArticleList from './components/ArticleList';
import Form from './components/Form';

function App() {

  const  [articles, setArticles] = useState([])
  const  [editArticle, setEditArticle] = useState(null)

  useEffect(() => {
      fetch('http://127.0.0.1:8009/articles/', {
        'method':'GET',
        headers:{
          'Content-Type':'application/json',
          'Authorization':'Token 2c3163e8ec5c8063907d13d69019b337542f0933'
        }
      })
      .then(resp => resp.json())
      .then(resp => setArticles(resp))
      .catch(error => console.log(error))

  }, [])

  const editBtn = (article) => {
    setEditArticle(article)
  }

  const updatedInformation = (article) => {
    const new_article = articles.map(myarticle => {
      if(myarticle.id === article.id){
        return article;
      }
      else {
        return myarticle;
      }
    })
    setArticles(new_article)
  }     //n   

  const articleForm = () => {
    setEditArticle({title:'', description:''})
  }

  const insertedInformation = (article) => {
    const new_articles = [...articles, article]
    setArticles(new_articles)
  }

  const deleteBtn = (article) => {
    const new_articles = articles.filter(myarticle => {
      if(myarticle.id === article.id){
        return false
      }
      return true;
    })
    setArticles(new_articles)
  }

  return (
    <div className="App">
        <div className='row'>
          <div className='col'>
            <h1>Django And ReactJS Course App</h1>
            <br></br>
          </div>
          <div className='col'>
          </div>
        </div>
        <ArticleList articles={articles} editBtn = {editBtn} deleteBtn = {deleteBtn }/>
        {editArticle ? <Form article = {editArticle} updatedInformation = {updatedInformation} insertedInformation = {insertedInformation}></Form> : null}
      
    </div>
  );
}

export default App;
