import React, { useEffect, useState } from 'react';
import "./clock.css"
export default function Clock() {
  const [value, setValue] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(
      () => setValue(new Date()),
      1000
    );

    return () => {
      clearInterval(interval);
    }
  }, []);
  return (
    <>
      <div className="box-element clock-container">
        {value.toDateString()}
      </div>
      <p className="time"> {value.toLocaleTimeString()} </p>

    </>
  )
}