import React from 'react'

const Registration = () => {
    const [Login,setLogin] = React.useState(true)
  return (
    <>
    <div className="border py-10 mt-20 w-[80%] max-w-[1000px] mx-auto  ">

<div className="w-1/2 mx-auto">

    <div className="grid grid-cols-2 gap-4">

    <button onClick={()=>setLogin(true)} className="w-full border py-2 rounded-md">login</button>
    
    <button onClick={()=>setLogin(false)} className="w-full border py-2 rounded-md">register</button>
    </div>

{Login ?
    <div className="flex flex-col">



    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Email or Username' />
    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Password' />
    <div className="grid grid-cols-2">

    <div className="flex mx-auto">
    <input class="form-check-input" type="checkbox" value="" id="loginCheck" checked />
    <label class="form-check-label" for="loginCheck"> Remember me </label>
    </div>
    <a href='#'>Forgot password?</a>
    </div>
    <button className="w-1/2 border py-2 rounded-md mx-auto my-4">Login</button>
    </div>

:
    <div className="flex flex-col">
    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Name' />
    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Username' />
    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Email' />
    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Password' />
    <input type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Repeat password' />
    <div className="flex gap-2">

    <input class="form-check-input" type="checkbox" value="" id="loginCheck" checked />
    <label class="form-check-label" for="loginCheck">I have read and agree to the terms</label>
    </div>
<button className="uppercase border rounded-md bg-blue-600 py-1 my-5">sign in</button>
    </div>
}

</div>
    </div>
    </>
  )
}

export default Registration