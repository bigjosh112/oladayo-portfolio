#!/usr/bin/env python3
"""Append portfolio projects to the original CV PDF without modifying pages 1-2."""

from __future__ import annotations

import textwrap
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(__file__).resolve().parent / "assets" / "Oladayo_Akinola_CV_source.pdf"
OUTPUT = ROOT / "public" / "files" / "Oladayo_Akinola_CV.pdf"

HEADER_COLOR = (0.1216, 0.2275, 0.3725)  # matches original CV blue
BODY_COLOR = (0.1333, 0.1333, 0.1333)
META_COLOR = (0.4, 0.4, 0.4)

MARGIN_X = 54
MARGIN_TOP = 54
LINE_HEIGHT = 13
SECTION_GAP = 10
PROJECT_GAP = 8

PORTFOLIO_PROJECTS = [
    {
        "title": "LoubbyAI - Talent & Payroll",
        "description": (
            "Global talent management, hiring, payroll, remittances, and employee "
            "management for African workforce with auth, payments, and wallet systems."
        ),
        "stack": "React, TypeScript, Next.js, Node.js, MongoDB",
        "link": "https://app.loubby.ai/",
    },
    {
        "title": "The Flex - Find Your Perfect Flexible Space",
        "description": (
            "Premium short-term rental platform for flexible spaces in desirable "
            "locations with booking and discovery workflows."
        ),
        "stack": "React, TypeScript, Next.js, Node.js, MongoDB",
        "link": "https://flex-living-frontend-timi.vercel.app/",
    },
    {
        "title": "Gopaddi - Travel, done your way",
        "description": (
            "Unified travel platform for booking, chat management, payments, and "
            "agency workflows from personal to business travel."
        ),
        "stack": "React, TypeScript, Next.js, Node.js, MongoDB",
        "link": "https://www.gopaddi.com/",
    },
    {
        "title": "Voyatek Group - Company Web App, Recruitment, CM",
        "description": (
            "Company landing page and admin app for job listings, applications, "
            "blog posts, subscriber data, and contact inquiries."
        ),
        "stack": "React, TypeScript, Next.js, Node.js, MongoDB",
        "link": "https://www.voyatekgroup.com/",
    },
    {
        "title": "Discova Trips",
        "description": (
            "Membership-based travel and activity platform with curated experiences, "
            "personalized activities, and premium membership tiers."
        ),
        "stack": "React, TypeScript, Next.js, Node.js, MongoDB",
        "link": "https://www.discovatrips.com/",
    },
    {
        "title": "Owambe - Enterprise Resource Planning",
        "description": (
            "Event organizer ERP with guest management, invitations, seating, orders, "
            "media sharing, wishlists, and guest PWA/scanner apps."
        ),
        "stack": "React, TypeScript, Next.js, Node.js, MongoDB",
        "link": "https://owambe-dashboard.vercel.app/dashboard",
    },
    {
        "title": "ShiftSync",
        "description": (
            "Team scheduling platform for shifts, availability, and coverage so teams "
            "stay in sync without chasing updates across chats."
        ),
        "stack": "Next.js, TypeScript, Tailwind, Node.js",
        "link": "https://shiftsync-frontend-tau.vercel.app/",
    },
    {
        "title": "Harmony Stores",
        "description": (
            "Nigerian retail technology storefront for computers, mobile phones, "
            "gadgets, and consumer electronics."
        ),
        "stack": "Next.js, TypeScript, Tailwind",
        "link": "https://www.harmonystores.ng/",
    },
]


def shorten(text: str, limit: int = 120) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def wrap_bullet(text: str, width: int = 92) -> list[str]:
    return textwrap.wrap(text, width=width) or [text]


def draw_line(
    page: fitz.Page,
    text: str,
    y: float,
    *,
    fontsize: float = 9,
    bold: bool = False,
    color: tuple[float, float, float] = BODY_COLOR,
    indent: float = 0,
) -> float:
    font = "helv" if not bold else "hebo"
    page.insert_text(
        (MARGIN_X + indent, y),
        text,
        fontname=font,
        fontsize=fontsize,
        color=color,
    )
    return y + LINE_HEIGHT


def build_pdf() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source CV not found: {SOURCE}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    source_doc = fitz.open(SOURCE)
    output_doc = fitz.open()

    for page_index in range(source_doc.page_count):
        output_doc.insert_pdf(source_doc, from_page=page_index, to_page=page_index)

    source_page = source_doc[0]
    page_rect = source_page.rect
    page = output_doc.new_page(width=page_rect.width, height=page_rect.height)

    y = MARGIN_TOP
    y = draw_line(page, "PORTFOLIO PROJECTS", y, fontsize=11, bold=True, color=HEADER_COLOR)
    y += SECTION_GAP

    for project in PORTFOLIO_PROJECTS:
        title = f'{project["title"]} — Portfolio'
        y = draw_line(page, title, y, fontsize=9.5, bold=True, color=BODY_COLOR)

        summary = shorten(project["description"])
        for line in wrap_bullet(summary):
            y = draw_line(page, f"• {line}", y, indent=12)

        stack_line = f'• Tech stack: {project["stack"]}'
        y = draw_line(page, stack_line, y, indent=12)

        link_line = f'• Link: {project["link"]}'
        y = draw_line(page, link_line, y, fontsize=8.5, color=META_COLOR, indent=12)

        y += PROJECT_GAP

        if y > page_rect.height - 72:
            page = output_doc.new_page(width=page_rect.width, height=page_rect.height)
            y = MARGIN_TOP

    output_doc.save(OUTPUT)
    output_doc.close()
    source_doc.close()

    print(f"Generated {OUTPUT} ({fitz.open(OUTPUT).page_count} pages)")


if __name__ == "__main__":
    build_pdf()
