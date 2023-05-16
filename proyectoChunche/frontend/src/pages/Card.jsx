import React, { Fragment } from 'react'
import temperaturaImagen from '../assets/temperaturaC.png'


function Card({titulo, valor}) {
    // const imgSource = "`./"+{atributo}+".png`"
  return (
    <Fragment>
        <div className="rounded-2xl shadow-2xl w-3/12 h-2/6 order-black border-2">
            {titulo}
            <img 
            className="w-18 h-20 mx-auto py-1"  
            src={temperaturaImagen}/>
            {valor}
        </div>
    </Fragment>
  )
}

export default Card