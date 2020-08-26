import React from "react";
import Navigation from "./Navigation";

function Header(props) {
  return (
    <header className="border-b p-4 flex justify-between items-center">
      <span className="font-bold">{props.appName}</span>

      <Navigation />
    </header>
  );
}

export default Header;
