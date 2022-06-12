export type User = {
  id: number;
  username: string;
};

export type UserLoginAPI = {
  email: string;
  password: string;
};

export type JWT = {
  access_token: string;
};
