import "./bg.css";

const Background = (props) => {
    return (
        <div className="animation-area">
            <ul className="box-area">
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
            </ul>
            {props.children}
        </div>
    );
}

export default Background;
