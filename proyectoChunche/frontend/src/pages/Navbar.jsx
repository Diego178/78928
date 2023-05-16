import React from 'react'
import { Link } from 'react-router-dom'


const Navbar = () => {
  return (
      <nav className="bg-gray-800 sticky">
        <div className="relative flex h-17 items-center justify-between">
          <div className="hidden sm:ml-6 sm:block flex-center">
            <div className="flex space-x-4">
              <Link className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-2 py-2 text-md font-medium"
                to='./Temperatura'>Temperatura</Link>

              <Link className="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-2 py-2 text-md font-medium"
               to='./Calidad'>Calidad</Link>

            </div>
          </div>

          </div>
      </nav>
  )
}

export default Navbar