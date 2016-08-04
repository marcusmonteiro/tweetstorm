import webpack from 'webpack'; // eslint-disable-line import/no-extraneous-dependencies
import webpackConfig from './webpack.config';

/**
 * Creates application bundles from the source files.
 */
function bundle() {
  const bundler = webpack(webpackConfig);
  bundler.run((err, stats) => {
    if (err) {
      throw err;
    }
    console.log(stats.toString(webpackConfig.stats)); // eslint-disable-line no-console
  });
}

export default bundle;
