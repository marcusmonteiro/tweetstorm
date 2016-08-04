import path from 'path';
import rmdir from 'rmdir';

const BUILD_DIR = path.join(__dirname, '..', 'build');

/**
 * Removes the output (build) directory.
 */
function clean() {
  rmdir(BUILD_DIR, (err) => {
    if (err && err.code !== 'ENOENT') {
      throw err;
    }
    console.log(`${BUILD_DIR} directory removed`); // eslint-disable-line no-console
  });
}

export default clean;
