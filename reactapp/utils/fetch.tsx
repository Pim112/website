import {JWT} from "../models";
import axios, {AxiosPromise} from "axios";

const basePath = "http://127.0.0.1:5000/api";

export enum FetchMethod {
  GET = "GET",
  POST = "POST",
  PUT = "PUT",
  DELETE = "DELETE",
}

export const defaultFetch = (
  pathname: string,
  method: FetchMethod,
  jwt?: JWT,
  body?: any
): AxiosPromise => {
  let headers: any = {
    "Content-Type": "application/json",
  };
  
  if (jwt?.access_token) {
    headers = {
      ...headers,
      Authorization: `Bearer ${jwt.access_token}`,
    };
  }
  const url = `${basePath}${pathname}`;
  const errorMessage = (reason: { message: any; response: any; }) => {
    console.log(
      `Axios fetch error on ${method} ${url}, error message: ${reason.message}`
    );
    return reason.response;
  };
  return method !== FetchMethod.GET ?
    axios({
      headers,
      method,
      url,
      data: body,
    }).catch((reason) => errorMessage(reason))
    :
    axios({
      headers,
      method,
      url,
      params: body,
    }).catch((reason) => errorMessage(reason))
};
