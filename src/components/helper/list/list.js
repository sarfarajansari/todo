import Postreq from "../request/post_request";
import "./list.css";
import {MdDone} from "react-icons/md"

const Checkbox=(props)=>{
    const complete=(e)=>{
        var p ="p" + String(props.index)
        var token = localStorage.getItem("taskToken")
        if(e.target.checked){
            e.target.checked=false
            document.getElementById(p).style.textDecoration="line-through"
            document.getElementById(p).style.textDecorationColor="rgba(15, 19, 66, 1)"
            document.getElementById(p).parentNode.style.animation="fade 0.8s linear forwards"
            Postreq("/todo/complete/",{"token":token,"id":props.task.id})
            setTimeout( props.update(0,token),50)
            setTimeout(()=>{
                document.getElementById(p).style.textDecoration="none"
                document.getElementById(p).parentNode.style.animation="none"
                document.getElementById(p).parentNode.style.opacity =1;
            },700)        
            
        }
        else{
            document.getElementById(p).style.textDecoration="none"
        }
    }
    const task = props.task
    if(!task.done){
        return(
            <input className="checkbox" type="checkbox" name={"task" + String(task.id)}  onClick={complete}/>
        )
    }
    return <MdDone color="rgb(0, 255, 0)"/>
}
const List = (props) => {
    return (
        <div className="list-container">
            {props.list.map((task,index)=>{
                var ms = (index * 300 ) +(300) -(30 * index);
                if(ms>7000){
                    ms=7000;
                }
                var delay =String(ms)+"ms" ;
                return(
                    <div className="list-item" style={{animationDuration:delay}}>
                        <div style={{background:"none"}}><Checkbox setdata={props.setdata} update={props.update} task={task} index={index}/> </div>
                         <p className="p" id={"p" + String(index)}>{task.task}</p>
                    </div>
                )
            })}
        </div>
    );
}

export default List;
