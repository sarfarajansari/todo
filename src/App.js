import "./App.css";
import Clock from "./components/helper/clock/clock";
import Background from "./components/helper/background/background";
import Nav from "./components/nav/nav";
import "./components/helper/typography/typography.css"
import Tasks from "./components/content/tasks";


function App() {
 
  return (
    <>
    <Background children={
      <div id="grid">
      <div id="navbar"><Nav/> </div>
      <div id="content">
        <Clock/>
        <Tasks/>
        

        </div>
      <div id="footer"><hr/></div>
    </div>
    }/>
    
    </>
  );
}

export default App;
