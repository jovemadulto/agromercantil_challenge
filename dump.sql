--
-- PostgreSQL database dump
--

\restrict qRSAainCjEcUc4z4xCyNUCTqzqEULkvPtX8wGNX5T1Get3XSsbukibwlGMB8hG1

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: acucar_cristal_branco_cepea_esalq_sao_paulo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acucar_cristal_branco_cepea_esalq_sao_paulo (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.acucar_cristal_branco_cepea_esalq_sao_paulo OWNER TO postgres;

--
-- Name: algodao_pluma_cepea_esalq_8_dias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.algodao_pluma_cepea_esalq_8_dias (
    date timestamp without time zone,
    prazo_de_8_dias_brl double precision,
    prazo_de_8_dias_usd double precision,
    region text
);


ALTER TABLE public.algodao_pluma_cepea_esalq_8_dias OWNER TO postgres;

--
-- Name: indicador_acucar_cristal_santos_fob; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_acucar_cristal_santos_fob (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_acucar_cristal_santos_fob OWNER TO postgres;

--
-- Name: indicador_arroz_casca_cepea_irga_rs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_arroz_casca_cepea_irga_rs (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_arroz_casca_cepea_irga_rs OWNER TO postgres;

--
-- Name: indicador_cafe_arabica_cepea_esalq; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_cafe_arabica_cepea_esalq (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_cafe_arabica_cepea_esalq OWNER TO postgres;

--
-- Name: indicador_cafe_robusta_cepea_esalq; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_cafe_robusta_cepea_esalq (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_cafe_robusta_cepea_esalq OWNER TO postgres;

--
-- Name: indicador_milho_esalq_bm_fbovespa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_milho_esalq_bm_fbovespa (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_milho_esalq_bm_fbovespa OWNER TO postgres;

--
-- Name: indicador_semanal_etanol_anidro_cepea_esalq_sao_paulo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_semanal_etanol_anidro_cepea_esalq_sao_paulo (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_semanal_etanol_anidro_cepea_esalq_sao_paulo OWNER TO postgres;

--
-- Name: indicador_semanal_etanol_hidratado_combustivel_cepea_esalq_s; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_semanal_etanol_hidratado_combustivel_cepea_esalq_s (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_semanal_etanol_hidratado_combustivel_cepea_esalq_s OWNER TO postgres;

--
-- Name: indicador_semanal_etanol_hidratado_outros_fins_cepea_esalq_s; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_semanal_etanol_hidratado_outros_fins_cepea_esalq_s (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_semanal_etanol_hidratado_outros_fins_cepea_esalq_s OWNER TO postgres;

--
-- Name: indicador_soja_cepea_esalq_parana; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_soja_cepea_esalq_parana (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_soja_cepea_esalq_parana OWNER TO postgres;

--
-- Name: indicador_soja_cepea_esalq_paranagua; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indicador_soja_cepea_esalq_paranagua (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.indicador_soja_cepea_esalq_paranagua OWNER TO postgres;

--
-- Name: preco_medio_trigo_cepea_esalq_parana; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.preco_medio_trigo_cepea_esalq_parana (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.preco_medio_trigo_cepea_esalq_parana OWNER TO postgres;

--
-- Name: preco_medio_trigo_cepea_esalq_rio_grande_sul; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.preco_medio_trigo_cepea_esalq_rio_grande_sul (
    date timestamp without time zone,
    a_vista_brl double precision,
    a_vista_usd double precision,
    region text
);


ALTER TABLE public.preco_medio_trigo_cepea_esalq_rio_grande_sul OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

\unrestrict qRSAainCjEcUc4z4xCyNUCTqzqEULkvPtX8wGNX5T1Get3XSsbukibwlGMB8hG1
