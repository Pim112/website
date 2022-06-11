import { JWT } from "../models";
import axios, { AxiosPromise } from "axios";

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
  body?: string
): AxiosPromise => {
  let headers: any = {
  };

  if (jwt?.access_token) {
    headers = {
      ...headers,
      Authorization: `Bearer ${jwt.access_token}`,
    };
  }
  const url = `${basePath}${pathname}`;

  return axios({
    headers,
    method,
    url,
    data: body,
  }).catch((reason) => {
    console.log(
      `Axios fetch error on ${method} ${url}, error message: ${reason.message}`
    );
    return reason.response;
  });
};
