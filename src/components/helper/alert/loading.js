import { Spin} from 'antd';
import "./alert.css"

const Loading = (props) => {
    return (
        <div className="spinner">
            <Spin size="large" spinning={props.loading}/>
        </div>
    );
}

export default Loading;
