import './App.css';
import axios from 'axios'
import {useState, useEffect} from 'react'
import Select from 'react-select'

function App() {
  const [nombresEmpresas, setNombresEmpresas] = useState([])
  const [empresaSeleccionada, setEmpresaSeleccionada] = useState("")
  const [liquidezGeneral, setLiquidezGeneral] = useState("")

  const getInfoEmpresa = () => {
    console.log(empresaSeleccionada)
    axios.post(process.env.REACT_APP_BASE_URL+`/api/getLiquidezGeneral`,{
      nombre: empresaSeleccionada
    }).then(res => setLiquidezGeneral(res.data))
  }

  useEffect(()=>{
    axios.get(process.env.REACT_APP_BASE_URL+`/api/getNombresEmpresas`).then(res => setNombresEmpresas(res.data))
  },[])
  console.log(nombresEmpresas)
  
  return (
    <div className="App" style={{display:"flex", flexDirection:"column", justifyContent:'center', alignItems:"center",marginTop:"50px"}}>
      <h1> Seleccione la empresa a revisar</h1>
      <div style={{width:'35vw'}}>
        <Select onChange={(empresaSeleccionada) => setEmpresaSeleccionada(empresaSeleccionada.value)} options={nombresEmpresas}/>
        <button className="button-17" role="button" onClick={() => getInfoEmpresa()}>Obtener información</button>
      </div>
      <h3>Liquidez General: {liquidezGeneral}</h3>
    </div>
  );
}

export default App;
