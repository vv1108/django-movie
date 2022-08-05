import './App.css';
import Layout from './components/layout/layout';

function App() {
  const url = 'http://127.0.0.1:8000/movies/index/';
  fetch(url, {
    headers : { 
      'Content-Type': 'application/json',
      'Accept': 'application/json'
     }
    }).then((res) => res.json()).then(data => console.log(data))
  return (
    <Layout>

    </Layout>
  );
}

export default App;
