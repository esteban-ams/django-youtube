import React from "react";
import "./tailwind.css";
import HelloWorld from "./Components/HelloWorld";
// import CounterExample from "./Components/CounterExampler";
import Header from "./Components/Header";

function App() {
  return (
    <div>
      <Header appName="my App" />

      <HelloWorld name="barry" laputa="que lo pario" />
    </div>
  );
}

export default App;
