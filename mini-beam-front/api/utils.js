import axios from 'axios';
import getConfig from "next/config";

const { publicRuntimeConfig } = getConfig();


export const getParamsData = (endpoint, params) => {
  let url;
  if (typeof window === 'undefined'){
    url = `${publicRuntimeConfig.API_SERVER_URL}${endpoint}`
  }else{
    url = `${publicRuntimeConfig.API_URL}${endpoint}`
  }
  return axios(url, {
    params,
    withCredentials: true,
  })
}