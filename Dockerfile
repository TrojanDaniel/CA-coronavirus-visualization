FROM continuumio/miniconda3

RUN git clone https://github.com/TrojanDaniel/CA-coronavirus-visualization

RUN conda install -c conda-forge yarn

RUN cd CA-coronavirus-visualization && yarn install

RUN pip install pandas

RUN pip install bokeh

WORKDIR CA-coronavirus-visualization

EXPOSE 5006

CMD ["bokeh", "serve", "--show", "resulting.py"]
