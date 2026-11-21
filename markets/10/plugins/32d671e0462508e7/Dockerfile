FROM node:22-bookworm-slim
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund
COPY src ./src
COPY skills ./skills
COPY data ./data
COPY examples ./examples
ENV CAROUSEL_HOST=0.0.0.0 CAROUSEL_PORT=8787
EXPOSE 8787
USER node
CMD ["node", "src/server.mjs"]
