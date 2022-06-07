import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react'
import ArticleList from './components/ArticleList';


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
        <ArticleList articles={articles}/>
    </div>
  );
}

export default App;
