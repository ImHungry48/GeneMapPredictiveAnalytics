import React from "react";

function Header() {
    return (
        <header className="header">
            <div className="logo">OG Insights</div>
            <img className="thumbnail" src='/thumbnail_image.png'/>
            <ul className="navigation">  
                {/* THROW IN NAVIGATION HERE */}
            </ul>
            
        </header>
    );
}

export default Header;