
const separator = '--------------------------------------------------------------------------------------';

class Logger {

  log = (): void => {

  }

  commit = (): void => {

  }

  write = (...str: [string]): void => {
    console.log(str.join(' '));
  }
}

export default Logger;
