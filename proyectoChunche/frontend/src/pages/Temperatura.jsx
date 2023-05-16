import React from "react";
import { useState, useEffect } from "react";
import axios from 'axios';


import Card from "./Card";

function Temperatura() {
  const [temperatura, setTemperatura] = useState({id:0, temperaturaC:""});
      useEffect(() =>{
        axios.get('/temperatura/ultimo')
        .then((response) => {
          setTemperatura(response.data)
          console.log(temperatura)
        }).catch(() => {
          alert('Algo fue mal...')
        })
      }, [])
  return (
    <>
      <div>Temperatura</div>
        <div className="w-full h-full flex items-center justify-center h-screen">
            <Card key={temperatura.id} titulo={"Temperatura Centigrados: "} valor={temperatura.temperaturaC}/>
        </div>
                    

    </>
  )
}

export default Temperatura