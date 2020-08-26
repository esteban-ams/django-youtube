import React from "react";
import "./tailwind.css";
import HelloWorld from "./Components/HelloWorld";
import Footer from "./Components/Footer";
import Header from "./Components/Header";

function App() {
  return (
    <div>
      <Header appName="my App" />

      <HelloWorld name="barry" laputa="que lo pario" />

      <Footer />
    </div>
  );
}

export default App;
