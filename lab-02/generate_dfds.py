"""Export Level 0 and Level 1 DFDs as high-resolution PNGs."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, FancyArrowPatch

OUT = Path(__file__).resolve().parent / 'diagrams'

def entity(ax, x, y, text, w=2.8, h=1.0):
    ax.add_patch(Rectangle((x-w/2, y-h/2), w, h, facecolor='white', edgecolor='black', lw=1.7))
    ax.text(x, y, text, ha='center', va='center', fontsize=11)

def process(ax, x, y, text, w=3.0, h=1.3):
    ax.add_patch(Ellipse((x,y),w,h,facecolor='#eaf2f8',edgecolor='black',lw=1.7))
    ax.text(x,y,text,ha='center',va='center',fontsize=11)

def store(ax, x, y, text, w=3.0, h=0.9):
    ax.plot([x-w/2,x+w/2],[y-h/2,y-h/2],color='black',lw=1.7)
    ax.plot([x-w/2,x+w/2],[y+h/2,y+h/2],color='black',lw=1.7)
    ax.text(x,y,text,ha='center',va='center',fontsize=11)

def flow(ax,a,b,label,offset=(0,0.18),rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,color='black',lw=1.3,connectionstyle=f'arc3,rad={rad}'))
    ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='center',fontsize=9,bbox=dict(facecolor='white',edgecolor='none',pad=1.5))

def canvas(title):
    fig,ax=plt.subplots(figsize=(12,8))
    ax.set_xlim(0,14); ax.set_ylim(0,10); ax.axis('off')
    ax.set_title(title,fontsize=16,pad=18)
    return fig,ax

def save(fig,name):
    fig.savefig(OUT/name,dpi=240,bbox_inches='tight',facecolor='white')
    plt.close(fig)

def main():
    OUT.mkdir(exist_ok=True)
    fig,ax=canvas('Level 0 Context DFD — Classroom Surveillance')
    entity(ax,1.8,5,'Camera')
    process(ax,7,5,'0\nSurveillance System',4,2)
    entity(ax,12,5,'Teacher / Operator')
    entity(ax,7,8.5,'Admin')
    flow(ax,(3.2,5),(5,5),'Video frames')
    flow(ax,(7,8),(7,6),'Settings',offset=(0.6,0))
    flow(ax,(9,5.4),(10.6,5.4),'Alerts / results',offset=(0,0.25))
    flow(ax,(10.6,4.6),(9,4.6),'Review decisions',offset=(0,-0.3))
    ax.text(7,1.2,'Entities = rectangles    Process = ellipse\nArrows = named data flows',ha='center',fontsize=10)
    save(fig,'dfd_level_0.png')

    fig,ax=canvas('Level 1 DFD — Object Detection and Analytics')
    entity(ax,1.7,8.6,'Camera',w=2.5)
    process(ax,5.5,8.6,'1.0\nData Ingestion')
    process(ax,10.8,8.6,'2.0\nPreprocessing')
    process(ax,10.8,5.6,'3.0\nModel Inference')
    process(ax,5.5,5.6,'4.0\nPost-processing')
    process(ax,5.5,2.3,'5.0\nStorage and Alerts')
    store(ax,1.7,5.6,'D1 Model Weights',w=2.8)
    store(ax,1.7,2.3,'D2 Event Store',w=2.8)
    entity(ax,10.8,2.3,'Teacher / Operator')
    entity(ax,1.7,0.7,'Admin',w=2.5,h=.8)
    flow(ax,(2.95,8.6),(4,8.6),'Raw frames')
    flow(ax,(7,8.6),(9.3,8.6),'Timestamped frame')
    flow(ax,(10.8,7.95),(10.8,6.25),'RGB tensor',offset=(.8,0))
    flow(ax,(3.1,5.8),(9.3,5.8),'Model parameters',offset=(0,.95),rad=-.2)
    flow(ax,(9.3,5.35),(7,5.35),'Raw predictions',offset=(0,-.2))
    flow(ax,(5.5,4.95),(5.5,2.95),'Filtered detections',offset=(1.2,0))
    flow(ax,(4,2.6),(3.1,2.6),'Event + evidence',offset=(0,.3))
    flow(ax,(3.1,2.05),(4,2.05),'Prior events',offset=(0,-.3))
    flow(ax,(7,2.6),(9.4,2.6),'Alerts / results',offset=(0,.3))
    flow(ax,(9.4,2.05),(7,2.05),'Review decisions',offset=(0,-.3))
    flow(ax,(2.95,.7),(4.8,1.7),'Settings',offset=(.35,-.05))
    ax.text(10.8,.5,'Rectangles: entities | Ellipses: processes\nParallel lines: stores | Arrows: data',ha='center',fontsize=9)
    save(fig,'dfd_level_1.png')
    print('Saved Level 0 and Level 1 DFD images.')

if __name__ == '__main__':
    main()
