import Getreq from "../request/get_request";
import Postreq from "../request/post_request";
import "./list.css";

const Checkbox=(props)=>{
    const complete=(e)=>{
        var p ="p" + String(props.index)
        var token = localStorage.getItem("taskToken")
        if(e.target.checked){
            document.getElementById(p).style.textDecoration="line-through"
            document.getElementById(p).style.textDecorationColor="rgba(15, 19, 66, 1)"
            document.getElementById(p).style.animation="fade 1s linear"
            Postreq("/todo/complete/",{"token":token,"id":props.task.id})
            var url = "/todo/get/0/"+token+"/" ;
            Getreq(url,props.setdata)
            
            
        }
        else{
            document.getElementById(p).style.textDecoration="none"
        }
    }
    const task = props.task
    if(!task.done){
        return(
            <input  type="checkbox" name={"task" + String(task.id)} onChange={complete}/>
        )
    }
}
const List = (props) => {
    return (
        <div className="list-container">
            

            {props.list.map((task,index)=>{
                var delay =String((index * 500) +500)+"ms" ;
                return(
                    <div style={{animationDuration:delay}}>
                        <div><Checkbox setdata={props.setdata} task={task} index={index}/> </div>
                         <p id={"p" + String(index)}>{task.task}</p>
                    </div>
                )
            })}
        </div>
    );
}

export default List;
