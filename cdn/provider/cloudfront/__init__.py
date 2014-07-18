"""CloudFront CDN Extension for CDN"""

from cdn.provider.cloudfront import driver

# Hoist classes into package namespace
CDNProvider = driver.CDNProvider
