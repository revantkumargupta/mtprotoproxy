services:
  - type: web
    name: telegram-mtproto
    env: docker
    dockerfilePath: Dockerfile
    branch: main
    autoDeploy: true
    envVars:
      - key: PORT
        value: "8443"           # Render assigns external port via $PORT env var
      - key: USERS
        value: '{"default": "<YOUR_SECRET_HEX>"}'
      - key: AD_TAG
        value: "<YOUR_AD_TAG_FROM_MTProxybot>"
