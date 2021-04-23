import React from "react";
import Head from 'next/head'
import PropTypes from "prop-types";


const  Header=({title, children})=>{
  return (
      <Head>
        <title>{title}</title>
        {children}
      </Head>
  )
}

Header.propTypes = {
  title: PropTypes.string,
}
Header.defaultProps={
  title: "Mini Beam Page",
}

export default Header;