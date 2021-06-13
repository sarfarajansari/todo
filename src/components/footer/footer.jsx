import React from 'react'
import {AiFillTwitterCircle,AiFillGithub} from "react-icons/ai"
import {CgInstagram} from "react-icons/cg"
import {ImLinkedin} from "react-icons/im"
import "./footer.css"

export default function Footer() {
    return (
        <div className="footer-container">
            <div className="tag">@2021 Sarfarajansari </div>
            <p style={{textAlign:"center",fontSize:"2rem",marginBottom:"1rem",color:"white"}}>Social</p>
            <div className="social-item">
                 <a href="https://twitter.com/Sarfraj49393426"><AiFillTwitterCircle  className="social-icon main"/><div className="social-name" >Twitter</div></a>
                 <a href="https://www.instagram.com/sarfarajansari_/"><CgInstagram className="social-icon main"/><div className="social-name">Instagram</div></a>
                 <a href="https://github.com/sarfarajansari"><AiFillGithub className="social-icon main"/><div className="social-name">Github</div></a>
                 <a href="https://www.linkedin.com/in/sarfaraj-ansari-a0a9441b9/"><ImLinkedin className="social-icon main"/><div className="social-name">LinkedIn</div></a>

             </div>
        </div>
    )
}
