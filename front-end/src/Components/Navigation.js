import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";

function Navigation() {
  const [showMenu, setShowMenu] = useState(false);
  let menu;
  let menuMask;
  if (showMenu) {
    menu = (
      <div className="fixed bg-white top-0 left-0 w-4/5 h-full shadow">
        Navigation Menu
      </div>
    );
    menuMask = (
      <div className="bg-black fixed top-0 left-0 w-4/5 h-full z-50"> </div>
    );
  }

  return (
    <nav>
      <span className="text-xl">
        <FontAwesomeIcon icon={faBars} onClick={() => setShowMenu(!showMenu)} />
      </span>
      {menu}

      {menuMask}
    </nav>
  );
}

export default Navigation;
