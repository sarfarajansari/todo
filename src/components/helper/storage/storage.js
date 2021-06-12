import React, { useState } from 'react';
const initialState = {
    alert:"sarfaraj"
}

export const Context = React.createContext();

const Storage = (props) => {
    const [state, setState] = useState(initialState)
    return (
        <Context.Provider value ={[state,setState]}>{props.children}</Context.Provider> 
    );
}

export default Storage;
