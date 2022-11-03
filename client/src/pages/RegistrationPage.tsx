import axios from 'axios';
import React, {useState,useRef} from 'react'

const RegistrationPage = () => {
    const [Login,setLogin] = React.useState(true)
    const loginEmail = useRef<HTMLInputElement>(null)
    const loginPassword = useRef<HTMLInputElement>(null)


    async function submitCredentials(path:string,data:Object) {
        axios.defaults.timeout = 10000;
        axios.defaults.timeoutErrorMessage = 'timeout';
        try {
            const response = await axios({
                method: 'POST',
                url: `http://localhost:5000/api/${path}`,
                headers: {
                    'Access-Control-Allow-Origin': '*',
               //Helpful in some cases.
               'Access-Control-Allow-Headers': '*',
               'Access-Control-Allow-Methods': '*',

                },
                data:data
            })
            console.log(response);
            if (response.status === 200) {
                setLogin(true);
            }
        } catch(error){

        }
    }

    async function submitUserCredentialsHandler(){
        const enteredLoginEmail = loginEmail.current?.value.trim();
        const enteredLoginPassword = loginPassword.current?.value.trim();


        const loginData = {
        user_email: enteredLoginEmail,
        user_password: enteredLoginPassword,
        };

        const feedback = await submitCredentials('login',loginData);
        return await feedback;
    }



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



    <input ref={loginEmail} type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Email or Username' />
    <input ref={loginPassword} type="text" className="border rounded-sm w-sm0%] my-4 py-2 pl-2 " placeholder='Password' />
    <div className="grid grid-cols-2">

    <div className="flex mx-auto">
    <input className="form-check-input" type="checkbox" value="" id="loginCheck" checked />
    <label className="form-check-label" htmlFor="loginCheck"> Remember me </label>
    </div>
    {/* <a href='#'>Forgot password?</a> */}
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

    <input className="form-check-input" type="checkbox" value="" id="loginCheck" checked />
    <label className="form-check-label" htmlFor="loginCheck">I have read and agree to the terms</label>
    </div>
<button className="uppercase border rounded-md bg-blue-600 py-1 my-5">sign in</button>
    </div>
}

</div>
    </div>
    </>
  )
}

export default RegistrationPage