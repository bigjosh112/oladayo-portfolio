This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

Repository: [github.com/bigjosh112/oladayo-portfolio](https://github.com/bigjosh112/oladayo-portfolio)

### Connect GitHub to Vercel

1. Go to [vercel.com/new](https://vercel.com/new) and sign in with GitHub.
2. Click **Import** next to `oladayo-portfolio`.
3. Keep the defaults (Next.js, `npm run build`, root `./`).
4. No environment variables are required.
5. Click **Deploy**.

Future pushes to `main` redeploy automatically.

### Post-deploy checklist

- Homepage shows your name and profile photo
- **Checkout my Resume** opens `/files/Oladayo_Akinola_CV.pdf`
- LinkedIn link works in the hero and footer
- Domain Expertise shows 4 cards (including AI Development)
- Projects and Experience sections render correctly

### Local production build

```bash
npm run build
npm start
```

### Optional: custom domain

In the Vercel project, open **Settings → Domains** and add your domain.
